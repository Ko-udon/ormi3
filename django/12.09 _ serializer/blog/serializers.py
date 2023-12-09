from rest_framework import serializers


# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(
#         max_length=10, 
#         error_messages={
#             'max_length': '제목은 10자를 초과할 수 없습니닷!',
#             'blank': '제목은 비워둘 수 없습니다.',
#             'required': '제목은 필수 항목입니다.'
#         }
#     )
#     content = serializers.CharField(
#         max_length=100,
#         error_messages={
#             'max_length': '내용은 100자를 초과할 수 없습니닷!',
#             'blank': '내용은 비워둘 수 없습니다.',
#             'required': '내용은 필수 항목입니다.'
#         }
#     )


# class PostSerializer(serializers.Serializer):
#     # 문자열 필드를 나타내며, 최대 10자까지 허용합니다.
#     title = serializers.CharField(
#         max_length=10,  # 최대 길이 설정
#         min_length=3,   # 최소 길이 설정, title은 최소 3자 이상이어야 함
#         allow_blank=False,  # 빈 문자열을 허용하지 않음
#         trim_whitespace=True  # 앞뒤 공백 자동 제거
#     )

#     # content 필드도 문자열 필드로 설정됩니다. 여기서는 최대 100자까지 허용됩니다.
#     content = serializers.CharField(
#         max_length=100,  # 최대 길이 설정
#         allow_null=True,  # null 값 허용, 필드가 비어 있어도 됨
#         default=''  # 기본값 설정, 명시적 값이 제공되지 않은 경우 빈 문자열을 사용
#     )
#     def validate_title(self, value):
#         """
#         validate_<field_name> 메서드를 사용하여 특정 필드에 대한 커스텀 유효성 검사를 수행합니다.
#         이 경우, 'title' 필드의 값에 'django'가 포함되어 있는지 확인합니다.
#         'django'가 포함되지 않은 경우, ValidationError가 발생합니다.
#         """
#         if 'django' not in value:
#             raise serializers.ValidationError('제목에 django가 없습니다.')
#         return value

#     def validate_content(self, value):
        
#         if '으헤' not in value:
#             raise serializers.ValidationError('내용에는 으헤가 들어가야됩니다.')
#         return value
    

#     def validate(self, data):
#         """
#         validate 메서드는 시리얼라이저 수준에서의 유효성 검사를 수행합니다.
#         이 메서드는 모든 필드에 대한 데이터가 포함된 딕셔너리를 받습니다.
#         여기서는 'title'과 'content' 필드가 서로 다른 값을 가지는지 확인합니다.
#         같은 값을 가질 경우 ValidationError를 발생시킵니다.
#         """
#         if data['title'] == data['content']:
#             raise serializers.ValidationError('제목과 내용이 같습니다.')
#         return data

from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=10)
    content = serializers.CharField(max_length=100)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['hello'] = 'hello world'
        return data